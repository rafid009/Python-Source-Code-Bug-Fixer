import numpy as np 

def function(x):

	k3 = 5
	j2 = 5
	paths = []
	try:
		if j2 >= 9:
			x = 2+3
			paths.append(1)
		else:
			j2 = 5-x
			x = x/1
			paths.append(2)
		if k3 <= 9:
			k3 = k3+3
			k3 = x+k3
			j2 = 0-0
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		j2 = k3**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))