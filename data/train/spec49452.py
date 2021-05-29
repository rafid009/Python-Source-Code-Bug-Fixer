import numpy as np 

def function(x):

	n9 = 9
	j5 = 1
	paths = []
	try:
		if x > 9:
			x = x/9
			n9 = n9+9
			j5 = n9+n9
			paths.append(1)
		else:
			j5 = 2/3
			x = j5+x
			j5 = x*j5
			paths.append(2)
		if x <= 2:
			n9 = 9/n9
			n9 = n9-j5
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		j5 = n9**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))