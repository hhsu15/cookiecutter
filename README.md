# Cookiecutter

https://cookiecutter.readthedocs.io/en/1.7.2/first_steps.html

## Installation

```bash
pip install cookiecutter

```

## Get started

```bash
$ mkdir HelloCookieCutter1
$ cd HelloCookieCutter1

```

Then, create a directory that looks like below. Looks weird, right?

```bash
$ mkdir {{cookiecutter.directory_name}}
$ cd {{cookiecutter.directory_name}}
```

Then, inside the {{cookiecutter.directory_name}}, create a file called {{cookiecutter.file_name}}.py

```bash
touch {{cookiecutter.file_name}}.py

# and edit the file you want, refer to our example

```

Then create a cookiecutter.json file and specify all the templated items!

```
cd ..
touch cookiecutter.json

```

```json
{
  "directory_name": "Hello",
  "file_name": "Howdy",
  "greeting_recipient": "Julie"
}
```

Now you can run the cookiecutter command and give it the directory of the cookiecutter project.

```bash
cd ..
cookiecutter HelloCookieCutter1
```

You will be promoted to fill in the templated variable names and you are all set!!

## hooks

Use hooks to run pre/post scripts. Create a folder called "hooks".

```
cookiecutter-something/
├── {{cookiecutter.project_slug}}/
├── hooks
│   ├── pre_gen_project.py
│   └── post_gen_project.py
└── cookiecutter.json

```

Refer to the file for how you can write the template.
