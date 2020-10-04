### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:            # this should use == not = as it's comparing a value not assigning one
      return True
    else                          # missing a : after else
      return False
   

  dif highest_card(self, card1 card2):          # this says dif not def - not creating the method, and there is no comma between card1 and card2
  if card1.value > card2.value:
    return card                                 # should say card1 not card
  else:
    return card2
  


def cards_total(self, cards):       # indentation level of the whole thing is off, isn't part of the CardGame class
  total                             # total should be assigned a value here for function to add to (eg. should say total = 0)
  for card in cards:
    total += card.value
    return "You have a total of" + total    #indentation is off, should be outside of for loop. cant add an integer to a string so total needs to be formatted
    
  
```
