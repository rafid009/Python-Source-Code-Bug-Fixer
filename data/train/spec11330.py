import numpy as np 

def function(x):

	q5 = x
	k3 = 7
	paths = []
	try:
		if k3 > 7:
			k3 = q5-k3
			q5 = x/5
			paths.append(1)
		else:
			k3 = 2/1
			k3 = k3*0
			paths.append(2)
		if x < 6:
			q5 = q5/q5
			paths.append(3)
		else:
			k3 = k3-8
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))