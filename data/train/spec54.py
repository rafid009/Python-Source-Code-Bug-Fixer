import numpy as np 

def function(x):

	j2 = x
	i1 = x
	paths = []
	try:
		if j2 <= 2:
			i1 = 8*i1
			paths.append(1)
		else:
			i1 = 5*i1
			paths.append(2)
		if j2 < 4:
			j2 = 2+9
			i1 = x-i1
			paths.append(3)
		else:
			j2 = 7*j2
			x = 9+2
			i1 = 6-i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		j2 = i1**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))