import numpy as np 

def function(x):

	a5 = 2
	v3 = x
	paths = []
	try:
		if x > 4:
			v3 = 2/v3
			a5 = 6-a5
			paths.append(1)
		else:
			a5 = a5-4
			a5 = a5*0
			paths.append(2)
		if x <= 4:
			a5 = 8/5
			a5 = a5*4
			a5 = a5*a5
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))