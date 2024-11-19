# SearchER-Film-Category-Database

### Film Category Database Software (SearchER) developed using Python with Tkinter module.

https://user-images.githubusercontent.com/87106402/198217567-e6676fb5-d3f6-41e7-836e-9d077bb5bd21.mp4

SearchER software is divided into two parts;

- <b>SearchER</b> **→** Use to **_Insert/Edit/Modify_** Movies and Movie Collections to/from the system.
- <b>SearchER - Search</b> **→** Use to _**View/Search/Filter**_ Movies and Movie Collections from the system.

![Screenshot 2022-05-25 122157](https://user-images.githubusercontent.com/87106402/170200165-7120cf42-dd71-4b4b-b2de-a7fa241826d5.png)

## SearchER

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/87106402/170200505-e83ec809-2ecb-4d21-976d-17183bf21aed.png" alt="Block Diagram">
</p>

### Features;

- Offline Use - Select the file directory that held movies or TV series at Local-drive.
- Insert Movies with their categories & language into the System (Database).
- 1100+ Movies (Categories & Language) Pre-configured to the system.
- Movie Collection - Insert/Remove Movies to/from Movie Collections.
<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/87106402/170202182-defaa5b8-2914-41ea-af0c-a1d585625ea1.png" alt="Block Diagram">
</p>
<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/87106402/170202505-732ba0ab-b1dd-4776-bff9-2af52950c6a4.png" alt="Block Diagram">
</p>

- Modify Database - Modify inserted data from the database (Change category/path of the movies and remove movies from the database).
<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/87106402/170202659-46e89b6a-2bd3-4dd2-a032-03470308f288.png" alt="Block Diagram">
</p>

## SearchER - Search

<p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/87106402/170204526-43f7d94a-71a6-4298-a307-775ea1b20c33.png" alt="Block Diagram">
  <img width="450" src="https://user-images.githubusercontent.com/87106402/170204893-9db819a5-cc68-4804-9e1c-e9f41281f0ab.png" alt="Block Diagram">
</p>

### Features;

- Search Movies or TV series by Name
<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/87106402/170209424-35fde237-eebb-4ab5-baf0-80ab65dacfc3.png" alt="Block Diagram">
</p>

- Filter by category of the Movies

  - Non-Combined Results - Show every movie that matched at least one category from user-selected categories.
  - Combined Results - Show every movie that matched all categories from user-selected categories.
  <p align="center">
    <img width="400" src="https://user-images.githubusercontent.com/87106402/170208663-ce2611d2-3e0e-4149-b119-5074d1c05363.png" alt="Block Diagram">
  </p>

- Movie Collection.
<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/87106402/170209006-33910e56-d08f-41a1-93f5-aa9b8ef4479c.png" alt="Block Diagram">
</p>

---

### Note

This was my first project, created during my self-learning journey with Python back in 2020. It has not been updated since then.

### Technical Details

- Database - SQLite
- Support operating systems (Tested) - Windows, Linux (Ubuntu)
- File Size - 28MB

### Ideas for Improvements

- Integrate OMDB API to fetch movie details
