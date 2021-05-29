import numpy as np 

def function(x):

	p1 = x
	k8 = x
	paths = []
	try:
		if k8 > 4:
			k8 = 0+k8
			k8 = k8-6
			x = x/x
			paths.append(1)
		else:
			x = 7*k8
			k8 = x+k8
			p1 = 3/k8
			paths.append(2)
		if p1 <= 9:
			x = 2-x
			paths.append(3)
		else:
			k8 = 0+x
			p1 = 5-0
			p1 = p1*3
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		k8 = p1**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))