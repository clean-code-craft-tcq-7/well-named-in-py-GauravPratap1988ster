from verify_num import verify_num
from verify_color import verify_color
from colour_referenceM import print_manual

if __name__ == '__main__':
  verify_num(4, 'White', 'Brown')
  verify_num(5, 'White', 'Slate')
  verify_color('Black', 'Orange', 12)
  verify_color('Violet', 'Slate', 25)
  verify_color('Red', 'Orange', 7)
  print_manual()
  print('Done :)')
