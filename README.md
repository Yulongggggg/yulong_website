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

The CV source is maintained in the dedicated
[`Yulong_CV2026_V2`](https://github.com/Yulongggggg/Yulong_CV2026_V2)
repository. After compiling that repository, copy the final PDF to both website
locations so the downloadable and embedded versions stay synchronized:

```sh
cp ../Yulong_CV2026_V2/Yulong_CV2026_V2.pdf assets/pdf/Yulong_CV2026_V2.pdf
cp ../Yulong_CV2026_V2/Yulong_CV2026_V2.pdf Yulong_CV2026_V2.pdf
```
