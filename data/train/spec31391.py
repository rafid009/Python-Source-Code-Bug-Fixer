import numpy as np 

def function(x):

	j3 = 5
	a3 = 4
	paths = []
	try:
		if a3 > 1:
			x = x+9
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x <= 9:
			x = 3-9
			a3 = a3*x
			a3 = a3*5
			paths.append(3)
		else:
			j3 = j3-6
			a3 = a3+3
			j3 = j3+4
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		j3 = a3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))