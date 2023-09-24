use std::fs;

pub fn get_profiles(path: String) -> std::io::Result<Vec<String>> {
//Read all directory names in the cwd/Profiles folder and return a vec with the names
    let pathlen = path.len()+1;
    return match fs::read_dir(path) {
        Ok(iterator) => {
            Ok(iterator.flat_map(|it| {
                match it {
                    Ok(entry) => {
                        //Get the folder name from the DirEntry
                        let pathname = entry.path().display().to_string();
                        let name = pathname[pathlen..].to_string();
                        Some(name)
                    }
                    Err(err) => panic!("{}", err.to_string())
                }
            }).collect())
        }
        Err(err) => { Err(err) }
    }
}