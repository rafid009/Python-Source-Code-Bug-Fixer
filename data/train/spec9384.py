import numpy as np 

def function(x):

	n2 = 7
	j2 = 4
	x = x
	paths = []
	try:
		if n2 >= 5:
			j2 = 5-j2
			paths.append(1)
		else:
			j2 = n2-4
			n2 = n2+9
			paths.append(2)
		if n2 >= 6:
			j2 = j2-4
			n2 = n2-5
			x = x/3
			paths.append(3)
		else:
			j2 = j2-3
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		n2 = j2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))