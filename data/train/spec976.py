import numpy as np 

def function(x):

	j2 = 3
	q8 = x
	paths = []
	try:
		if x > 4:
			j2 = j2+5
			j2 = j2*j2
			paths.append(1)
		else:
			x = x-4
			j2 = 6+5
			j2 = 5+4
			paths.append(2)
		if q8 > 2:
			q8 = 0/j2
			j2 = j2/x
			paths.append(3)
		else:
			x = x+2
			j2 = j2+x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		q8 = j2**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))