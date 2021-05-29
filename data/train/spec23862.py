import numpy as np 

def function(x):

	p1 = 4
	k8 = x
	paths = []
	try:
		if x <= 4:
			p1 = 5-p1
			x = k8*x
			paths.append(1)
		else:
			x = 8*5
			k8 = 3*k8
			x = x+8
			paths.append(2)
		if k8 > 6:
			x = x/2
			paths.append(3)
		else:
			p1 = p1+0
			x = x+x
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		k8 = k8**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))