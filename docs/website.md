# Website Deployment

After the first successful deployment, the public presentation is available at https://sagarb3.github.io/ui-engineer-skill/.

Edit `README.html` to update the website. The GitHub Pages workflow copies that file to the deployment artifact as `index.html`; no separate page source or build dependency is needed. Documentation links point to rendered repository files on GitHub.

The workflow deploys when `README.html` or `.github/workflows/pages.yml` changes on `main`. It can also be run manually from the Actions tab. Only the prepared HTML page is uploaded; skill packages and repository tooling remain in the repository.

A repository owner must select **Settings → Pages → Build and deployment → Source → GitHub Actions** once before deployment. If the initial workflow ran before this setting was enabled, use **Re-run all jobs** on that run. The repository's Pages publishing source must be GitHub Actions. Deployment uses the `github-pages` environment and the job's Pages and OpenID Connect permissions. Changes do not require a custom domain or additional credentials.

Inspect the deployment workflow and environment to check status. To roll back page content, revert the relevant HTML change through normal Git review and push to `main`. The repository homepage continues to display `README.md`, which links to the website.
