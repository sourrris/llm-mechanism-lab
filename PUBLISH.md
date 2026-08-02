# Publish this forge to GitHub

The repository already contains a `main` branch and an initial commit.

## One-command publish

Install and authenticate GitHub CLI once:

```bash
brew install gh
gh auth login
```

From the repository root:

```bash
./scripts/publish_to_github.sh llm-mechanism-lab public
```

That command will:

1. Create `sourrris/llm-mechanism-lab` if it does not exist.
2. Push the committed `main` branch.
3. Create the labels `day`, `evidence`, `blocked` and `research`.
4. Create one evidence-gated GitHub issue for each of the fourteen days.

Use `private` instead of `public` as the second argument when needed.

## Manual fallback

```bash
gh repo create sourrris/llm-mechanism-lab --public --source=. --remote=origin --push
./scripts/setup_github_issues.sh sourrris/llm-mechanism-lab
```

Do not upload files individually through the browser. Preserve the commit history and executable permissions by publishing the repository itself.
