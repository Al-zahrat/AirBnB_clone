<h1>Welcome to the AirBnB clone project!</h1>

<h2>Description of the project:</h2>
<p>The Airbnb clone project is a simple copy of the Airbnb Website</p>
<h2>Command interpreter</h2>
<h3>The clone porject contains:</h3>
<ul>
<li>A parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>A simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file</li>
<li>All classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel</li>
<li>The first abstracted storage engine of the project: File storage.</li>
<li>All unittests to validate all our classes and storage engine</li>
</ul>
<h3>How to start it and How to use it:</h3>
<p>Type ./console.py to start the console
<br>and type help to see the available commands</p>
<h3>Examples</h3>
<code>
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
</code>
<h2>Authors:</h2>
EZZAHRA EL IDRISSI
