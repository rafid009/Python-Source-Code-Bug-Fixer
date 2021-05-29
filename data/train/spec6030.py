import numpy as np 

def function(x):

	v2 = 4
	i1 = 7
	paths = []
	try:
		if v2 <= 7:
			i1 = 4-i1
			x = 5*v2
			v2 = v2-6
			paths.append(1)
		else:
			i1 = i1/9
			v2 = v2-0
			x = i1/5
			paths.append(2)
		if i1 > 7:
			v2 = v2+6
			v2 = v2/4
			paths.append(3)
		else:
			x = 7*x
			i1 = 2/i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))