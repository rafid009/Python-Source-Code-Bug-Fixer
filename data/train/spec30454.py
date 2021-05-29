import numpy as np 

def function(x):

	q5 = x
	f9 = x
	paths = []
	try:
		if q5 < 4:
			x = x*0
			paths.append(1)
		else:
			f9 = x+1
			paths.append(2)
		if x < 5:
			f9 = q5-f9
			x = f9-q5
			paths.append(3)
		else:
			q5 = 8*4
			x = x+x
			f9 = f9*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))