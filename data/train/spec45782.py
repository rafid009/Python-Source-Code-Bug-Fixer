import numpy as np 

def function(x):

	j3 = x
	d0 = 4
	paths = []
	try:
		if x <= 0:
			x = x*d0
			x = d0+7
			j3 = j3-6
			paths.append(1)
		else:
			d0 = d0+2
			x = j3-x
			paths.append(2)
		if j3 > 1:
			x = d0-d0
			d0 = d0/7
			x = 2+x
			paths.append(3)
		else:
			x = 7-9
			x = x+x
			d0 = d0-9
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