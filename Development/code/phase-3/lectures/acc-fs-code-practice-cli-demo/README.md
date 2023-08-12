# acc-fs-demo-cli-build

[Toy Tracker ERD](https://drive.google.com/file/d/1WKy2iVEmagAvpYfBiemhxC2j47lx9_mJ/view?usp=sharing)

## Deliverables

- Create a point of entry. 
    - Create a `cli.py` file.
    -  Add a function, `start()` that welcomes the user and prints a set of options:
        - My Toys (Get all toys related to current user)
        - Add Toy
        - Exit 
- Add some flare
    - color terminal: https://github.com/noyoshi/prettycli
    - menu selection: https://github.com/IngoMeyer441/simple-term-menu#create-a-menu-with-the-default-style
    - ASCII Terminal Art: https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=toy%20tracker
    - Create a function that returns a welcome banner.
    - Clear screen


- BREAK: https://docs.google.com/presentation/d/1qv0zKYWCgX2uOgNwgDhtRY3MTy61SZPvbCLO0YpAcus/edit#slide=id.g26104cc7a0e_0_28



- Refactor using a class
    - Create a CLI class
    - Create start method using menu selection
    - Handle selection
- My Toys Option
    - Render all toys associated with the first Owner (no login)
- Create new toy
    - Collect toy information
        - name
        - manufacturer 
        - type
        - associate with user 1 (no login)
        - Show it in my toys
- Deleting a Toy

