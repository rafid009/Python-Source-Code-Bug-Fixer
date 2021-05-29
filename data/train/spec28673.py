import numpy as np 

def function(x):

	b3 = x
	r3 = 7
	paths = []
	try:
		if r3 <= 3:
			r3 = r3+5
			r3 = 3*5
			r3 = r3-5
			paths.append(1)
		else:
			r3 = r3/4
			paths.append(2)
		if r3 < 8:
			b3 = b3/4
			x = 1*0
			paths.append(3)
		else:
			x = x+3
			r3 = r3*7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		r3 = b3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))