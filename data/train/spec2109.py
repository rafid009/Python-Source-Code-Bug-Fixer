import numpy as np 

def function(x):

	j3 = x
	o6 = x
	paths = []
	try:
		if o6 < 6:
			x = j3-o6
			paths.append(1)
		else:
			x = o6/6
			j3 = 5/o6
			paths.append(2)
		if o6 > 4:
			o6 = 9+o6
			o6 = 0/o6
			o6 = o6-j3
			paths.append(3)
		else:
			j3 = j3+6
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))