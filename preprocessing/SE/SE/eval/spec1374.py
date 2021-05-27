import numpy as np 

def function(x):

	j3 = x
	p4 = 7
	paths = []
	try:
		if x >= 1:
			p4 = 5+p4
			x = x*p4
			j3 = j3-p4
			paths.append(1)
		else:
			j3 = 9-j3
			x = 0/x
			p4 = x-p4
			paths.append(2)
		if x <= 7:
			j3 = j3+1
			x = 6*8
			x = 1/7
			paths.append(3)
		else:
			x = p4*x
			p4 = 8+p4
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		p4 = j3**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))