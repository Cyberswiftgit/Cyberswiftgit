
# Profile Repository Setup

## Requirements

- A public GitHub repository named `Cyberswiftgit`
- A root-level `README.md`
- GitHub Actions enabled

## Browser-only installation

1. Open the repository on GitHub.
2. Select Add file → Create new file.
3. Enter the required file path, including directories.
4. Paste the contents and commit the change.
5. Repeat for each file in the project structure.

## Enable the contribution animation

1. Open Settings → Actions → General.
2. Set workflow permissions to Read and write.
3. Open Actions.
4. Run Generate contribution snake manually.
5. Confirm the output branch exists.

## Customize the profile

- Edit the introduction in README.md.
- Edit assets/profile.svg for the terminal banner.
- Edit assets/skills.svg for the radar design.
- Edit assets/skills.json for your own skill ratings.
- Add actual project links only after the corresponding repositories exist.

## Troubleshooting

- Broken images: check the filename, capitalization, and repository visibility.
- Missing snake: check the Actions run and the output branch.
- Workflow cannot push: verify repository Actions permissions.
- Statistics unavailable: the external statistics service may be rate-limited.

