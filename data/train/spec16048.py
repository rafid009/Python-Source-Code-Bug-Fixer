import numpy as np 

def function(x):

	d9 = 0
	j2 = 7
	paths = []
	try:
		if d9 >= 0:
			j2 = 4+9
			d9 = x+j2
			x = 4+x
			paths.append(1)
		else:
			x = x+7
			x = d9*d9
			paths.append(2)
		if d9 >= 8:
			j2 = 0-j2
			x = 9-x
			paths.append(3)
		else:
			j2 = j2/d9
			j2 = j2-7
			d9 = d9-6
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		d9 = j2**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))