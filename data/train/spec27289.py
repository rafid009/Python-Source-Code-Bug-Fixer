import numpy as np 

def function(x):

	j3 = x
	d5 = 3
	paths = []
	try:
		if j3 > 4:
			d5 = 8/3
			paths.append(1)
		else:
			d5 = d5-x
			d5 = d5*2
			d5 = 4*5
			paths.append(2)
		if d5 <= 4:
			j3 = 7*x
			j3 = j3-d5
			paths.append(3)
		else:
			j3 = j3/x
			d5 = d5-3
			j3 = 8-d5
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