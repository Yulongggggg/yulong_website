# Yulong Liu - Personal Website

Academic portfolio built with Jekyll and deployed to GitHub Pages.

## Local development

```sh
bundle install --path vendor/bundle
bundle exec jekyll serve
```

The configured local URL is `http://127.0.0.1:4000/yulong_website/`.

## Build

```sh
bundle exec jekyll build
```

## Update the CV PDF

The website CV is generated from a versioned Python script so the downloadable and embedded files stay synchronized.

```sh
python3 scripts/build_cv.py
```

The generated web copy is written to `assets/pdf/Yulong_CV2026_V2.pdf`.
