import numpy as np 

def function(x):

	o5 = 9
	j1 = 7
	paths = []
	try:
		if x <= 3:
			x = j1-o5
			j1 = 0*j1
			paths.append(1)
		else:
			o5 = o5+5
			paths.append(2)
		if j1 < 2:
			j1 = j1*2
			paths.append(3)
		else:
			j1 = 0-9
			o5 = 3-x
			o5 = x/3
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		o5 = j1**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))