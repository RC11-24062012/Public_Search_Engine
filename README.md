# Mishika_Hirwani
RC11 Public Search Engine (2025)

This is the open-source collaborative search engine platform for Bartlett RC11, showcasing resources uploaded by members including images, texts, models, etc. It supports tag-based search, categorized browsing, and automatic deployment.

Online Access:  
[https://your-username.github.io/your-repo-name/](https://rc11-24062012.github.io/Public_Search_Engine/)


Project Structure Overview (Standardized Format)

├── index.html                 ← Frontend main page (search interface)

├── search.js                  ← Frontend logic: loads and renders tags.json

├── merge_tags.py              ← Admin: merges data from all members

├── requirements.txt           ← Python dependencies (can be empty)

├── data/

│   ├── tags.json              ← Main tag file (auto-merged, used by frontend)

│   ├── huanqi/

│   │   ├── tags.json          ← Each member's data entry point

│   │   ├── 001.jpg            ← Images go directly into the user folder

│   │   ├── model.glb          ← Models are also placed here

│   │   └── drawing.pdf        ← PDFs are placed in the same way

│   ├── yutong/

│   └── ...

└── .github/

    └── workflows/
    
        └── deploy.yml         ← Auto-deployment script (GitHub Actions)


Submission Guidelines (Required for All Members)

All images, models, documents, etc. must be placed directly in your personal folder. Do not create subfolders.

Correct structure example:

data/huanqi/
├── tags.json
├── room.jpg
├── plan.pdf
└── scene.glb

Incorrect structure (subfolders like images, pdf, or models are not allowed):

data/huanqi/images/room.jpg       
data/huanqi/models/scene.glb      


tags.json Format Requirements (Example)

{
  "files": {
    "room.jpg": {
      "type": "image",
      "tags": ["minimal", "white", "interior"],
      "title": "My Room",
      "source": "huanqi"
    },
    "scene.glb": {
      "type": "model",
      "tags": ["3d", "structure"],
      "title": "GLB Model",
      "source": "huanqi"
    }
  }
}


Workflow for Contributors

1. Fork this repository  
2. In data/your-name/, upload:
   - tags.json
   - All images / models / PDFs (directly into the folder)
3. Submit a Pull Request  
4. Once merged by an admin, the website will be automatically updated


Automatic Deployment (CI/CD)

Each time a PR is merged, GitHub Actions will automatically:

- Set up the Python environment
- Run merge_tags.py to merge all member data
- Update data/tags.json
- Deploy the updated site to GitHub Pages

You can view the logs on the GitHub Actions page.


Admin Instructions

Admins should:

- Review and merge member PRs
- Ensure folder names are lowercase and contain no subfolders
- Optionally run merge_tags.py locally for final verification


Enabled Features

- Multi-tag search  
- Data merge script (preserves original structure and fills in missing image fields)  
- GitHub Pages auto-deployment  
