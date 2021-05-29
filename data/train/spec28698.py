import numpy as np 

def function(x):

	f8 = 4
	o5 = 6
	paths = []
	try:
		if x < 8:
			f8 = f8*2
			o5 = 5-o5
			paths.append(1)
		else:
			o5 = o5*o5
			f8 = f8+3
			paths.append(2)
		if f8 >= 3:
			x = x*0
			x = 3*x
			paths.append(3)
		else:
			f8 = f8*8
			x = f8-4
			f8 = 0/8
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))