use std::{env, fs, io, path::{Path, PathBuf}, process};

const PROFILES: &[(&str, &[&str])] = &[
    ("library", &["source", "tests", "examples", "documentation"]),
    ("application", &["source", "tests", "configuration", "documentation", "deployment"]),
    ("service", &["source", "tests", "configuration", "specifications", "infrastructure", "deployment", "documentation"]),
    ("cli", &["source", "tests", "examples", "documentation"]),
    ("monorepo", &["source", "tests", "examples", "tools", "scripts", "configuration", "documentation", "specifications", "infrastructure", "deployment"]),
];

fn profile_dirs(profile: &str) -> Option<&'static [&'static str]> {
    PROFILES.iter().find(|(name, _)| *name == profile).map(|(_, dirs)| *dirs)
}

fn safe_name(value: &str) -> Result<String, String> {
    let cleaned = value.trim().replace(['/', '\\'], "-");
    if cleaned.is_empty() || cleaned == "." || cleaned == ".." {
        return Err("repository name must not be empty or a path traversal value".into());
    }
    if cleaned.chars().any(|ch| ch.is_control()) {
        return Err("repository name contains a control character".into());
    }
    Ok(cleaned)
}

fn write_file(path: &Path, content: &str) -> io::Result<()> {
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent)?;
    }
    fs::write(path, content)
}

fn create_structure(destination: &Path, profile: &str, name: &str) -> io::Result<usize> {
    if destination.exists() {
        return Err(io::Error::new(io::ErrorKind::AlreadyExists, format!("destination already exists: {}", destination.display())));
    }
    fs::create_dir_all(destination)?;
    let mut count = 0;

    for directory in profile_dirs(profile).expect("validated profile") {
        let dir = destination.join(directory);
        fs::create_dir_all(&dir)?;
        write_file(&dir.join(".gitkeep"), "")?;
        println!("  {}/", directory);
        count += 1;
    }

    write_file(&destination.join("README.md"), &format!("# {name}\n\nCreated from Ecosystem Foundation profile `{profile}`.\n"))?;
    write_file(&destination.join(".gitignore"), "# Generated/build output\n.env\n.env.*\n*.log\ncoverage/\ndist/\nbuild/\ntarget/\n")?;
    let metadata = format!(
        "{{\n  \"foundation\": \"ecosystem-foundation\",\n  \"foundation_contract\": \"0.2\",\n  \"profile\": \"{profile}\",\n  \"name\": \"{name}\"\n}}\n"
    );
    write_file(&destination.join(".ecosystem.json"), &metadata)?;
    println!("  README.md\n  .gitignore\n  .ecosystem.json");
    Ok(count + 3)
}

fn print_usage() {
    println!("Usage: ecosystem-init <profile> <name> [--path <destination>]");
    println!("Profiles: {}", PROFILES.iter().map(|(name, _)| *name).collect::<Vec<_>>().join(", "));
}

fn main() {
    let mut args = env::args().skip(1);
    let Some(profile) = args.next() else {
        print_usage();
        process::exit(2);
    };
    let Some(raw_name) = args.next() else {
        print_usage();
        process::exit(2);
    };
    let name = safe_name(&raw_name).unwrap_or_else(|e| {
        eprintln!("error: {e}");
        process::exit(2);
    });

    let mut path = None;
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--path" => {
                path = Some(PathBuf::from(args.next().unwrap_or_else(|| {
                    eprintln!("error: --path requires a value");
                    process::exit(2);
                })));
            }
            "--help" | "-h" => {
                print_usage();
                return;
            }
            other => {
                eprintln!("error: unknown argument: {other}");
                process::exit(2);
            }
        }
    }

    if profile_dirs(&profile).is_none() {
        eprintln!("error: unknown profile `{profile}`");
        print_usage();
        process::exit(2);
    }

    let destination = path.unwrap_or_else(|| PathBuf::from(&name));
    match create_structure(&destination, &profile, &name) {
        Ok(count) => println!("created {} ({} paths)", destination.display(), count),
        Err(error) => {
            eprintln!("error: {error}");
            process::exit(1);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rejects_traversal_names() {
        assert!(safe_name("").is_err());
        assert!(safe_name(".").is_err());
        assert!(safe_name("..").is_err());
        assert_eq!(safe_name("a/b").unwrap(), "a-b");
    }

    #[test]
    fn profiles_are_complete() {
        let names: Vec<_> = PROFILES.iter().map(|(name, _)| *name).collect();
        assert_eq!(names, vec!["library", "application", "service", "cli", "monorepo"]);
    }

    #[test]
    fn creates_library_shape() {
        let root = env::temp_dir().join(format!("ecosystem-init-test-{}", process::id()));
        let _ = fs::remove_dir_all(&root);
        let count = create_structure(&root, "library", "demo").unwrap();
        assert!(root.join("source/.gitkeep").exists());
        assert!(root.join("tests/.gitkeep").exists());
        assert!(root.join("README.md").exists());
        assert!(root.join(".ecosystem.json").exists());
        assert_eq!(count, 7);
        fs::remove_dir_all(root).unwrap();
    }
}
