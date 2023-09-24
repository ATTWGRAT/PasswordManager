mod fileio;

use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn getProfiles(path: String) -> PyResult<Vec<String>> {
    Ok(fileio::get_profiles(path)?)
}

/// A Python module implemented in Rust.
#[pymodule]
fn PasswordManager(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(getProfiles, m)?)?;
    Ok(())
}