import numpy as np 

def function(x):

	j2 = x
	d9 = 3
	x = x
	paths = []
	try:
		if d9 <= 3:
			x = x*6
			d9 = j2/j2
			j2 = 1/j2
			paths.append(1)
		else:
			d9 = d9+9
			paths.append(2)
		if d9 >= 6:
			d9 = x*6
			x = x-5
			paths.append(3)
		else:
			x = 6+x
			d9 = 6+9
			d9 = d9-2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))