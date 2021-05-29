import numpy as np 

def function(x):

	k8 = x
	p8 = 5
	paths = []
	try:
		if x < 1:
			x = x*1
			paths.append(1)
		else:
			x = 2/7
			p8 = 3+7
			paths.append(2)
		if x > 2:
			p8 = k8/4
			paths.append(3)
		else:
			x = x/8
			p8 = p8-1
			x = x/6
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		p8 = k8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))