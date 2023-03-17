# Instruction to create the database

#### After this run the code `python manage.py makemigration` to create the instruction for the migration

#### Then run the command `python manage.py migrate` to create the db

#### Run `python manage.py shell` it open up the shell where we can write the python command that gets executed in this web application

#### Then in the shell type `from flights.model import */Flight`

                                # app.file           Class

#### Then we can create the new flight just this:

#### `f= Flight(origin="Kathmandu", destination= "Japan", duration=415)`

#### Then do `f.save()`

#### And for the query purpose we can do multiple things like:

#### `Flights.object.all()`

#### or...

#### `flights = Flights.object.all()` ----><QuerySet>

#### `flight = flights.first()`

#### `flight.id`

#### `flight.origin`

#### `flight.destination`

#### `flight.duration`

#### And to delete the flight we can say `flight.delete()`

#### We can conduct the filter for example `Airport.objects.filter(city="Tokyo")` ----><QuerySet>

#### We can do this when we know there is only gonna be the one result for the query:

#### `Airport.objects.get(city="Tokyo")`

#### To simplity this process there is easier method in the django

#### we can use the admin panel of the django

#### `python manage.py createsuperuser`

#### The first thing to do after this is to take the model and add it to the `admin` app in main file
