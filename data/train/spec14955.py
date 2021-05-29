import numpy as np 

def function(x):

	v6 = 5
	j9 = x
	paths = []
	try:
		if j9 >= 7:
			j9 = v6+j9
			x = 3*x
			paths.append(1)
		else:
			v6 = x+v6
			j9 = x/4
			j9 = v6-2
			paths.append(2)
		if v6 < 2:
			v6 = v6+7
			paths.append(3)
		else:
			v6 = 6-v6
			v6 = v6-4
			v6 = x-2
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		j9 = v6**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))