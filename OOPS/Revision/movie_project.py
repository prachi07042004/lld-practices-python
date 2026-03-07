class Movie:

  def __init__(self, movie_name:str, total_seats: int, ticket_price: float)-> None:
    self.movie_name = movie_name
    self.total_seats = total_seats #total seats available in theatre
    self.ticket_price = ticket_price #price per ticket
    self.booked_seats = 0 

  def book_tickets(self, num_tickets: int)-> None:
    if num_tickets > self.total_seats - self.booked_seats:
      print("Sorry, not enough seats available!")
    else:
      self.booked_seats += num_tickets #we have added the tickets to be booked in the existing booked seats
      self.total_seats -= num_tickets
      print("Your ticket is booked!")
      print(f"Total amount to pay: {self.ticket_price * num_tickets}")



  def show_status(self) -> None:
    print(f"Movie : {self.movie_name}")
    print(f"Seats Available: {self.total_seats}")
    print(f"Total booked: {self.booked_seats}\n")
 

movie = Movie("3 idiots", 100, 499)
movie.show_status()
# movie.book_tickets(250)
movie.book_tickets(70)

movie.show_status()

movie.book_tickets(70)
