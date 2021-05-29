import numpy as np 

def function(x):

	p4 = x
	k5 = 5
	paths = []
	try:
		if k5 <= 4:
			x = x/8
			p4 = p4+2
			k5 = 3-k5
			paths.append(1)
		else:
			p4 = 3+p4
			x = x*0
			k5 = k5/k5
			paths.append(2)
		if x > 6:
			k5 = x*k5
			p4 = 6+0
			paths.append(3)
		else:
			k5 = p4+1
			x = x-4
			p4 = k5/k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		p4 = k5**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))