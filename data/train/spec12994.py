import numpy as np 

def function(x):

	o2 = 4
	j0 = 3
	x = 1
	paths = []
	try:
		if x > 0:
			x = x/6
			j0 = 0-j0
			paths.append(1)
		else:
			x = o2*0
			x = x/x
			j0 = j0-5
			paths.append(2)
		if j0 <= 7:
			o2 = o2*5
			x = x/j0
			paths.append(3)
		else:
			o2 = o2+x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))