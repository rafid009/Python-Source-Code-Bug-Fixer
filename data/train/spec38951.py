import numpy as np 

def function(x):

	f1 = 0
	p2 = x
	paths = []
	try:
		if p2 < 6:
			x = p2+4
			x = p2+x
			paths.append(1)
		else:
			p2 = p2+1
			f1 = 0/5
			paths.append(2)
		if x <= 0:
			x = f1*x
			p2 = p2-9
			f1 = p2-8
			paths.append(3)
		else:
			p2 = p2+p2
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		p2 = f1**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))