import numpy as np 

def function(x):

	p6 = x
	t4 = 6
	x = x
	paths = []
	try:
		if t4 >= 5:
			t4 = t4-5
			p6 = 4-p6
			x = p6-x
			paths.append(1)
		else:
			p6 = x-8
			t4 = 2+t4
			paths.append(2)
		if x <= 5:
			p6 = p6-1
			paths.append(3)
		else:
			t4 = t4/t4
			p6 = p6+x
			p6 = 5+0
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))