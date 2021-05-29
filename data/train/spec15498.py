import numpy as np 

def function(x):

	v6 = x
	j2 = 7
	paths = []
	try:
		if v6 <= 3:
			v6 = x/1
			paths.append(1)
		else:
			j2 = j2-j2
			paths.append(2)
		if j2 >= 1:
			x = x+j2
			paths.append(3)
		else:
			v6 = v6/3
			v6 = 6-9
			v6 = 9-x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		j2 = v6**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))