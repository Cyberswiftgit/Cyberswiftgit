
param(
    [string]$Username = "Cyberswiftgit"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$readme = Join-Path $root "README.md"

if (-not (Test-Path $readme)) {
    throw "README.md not found in $root"
}

Write-Host "Profile repository: $Username"
Write-Host "README found: $readme"
Write-Host "Open README.md and update your project links before publishing."

