import numpy as np 

def function(x):

	u8 = x
	p1 = 5
	paths = []
	try:
		if u8 < 4:
			x = x/x
			x = 0+x
			paths.append(1)
		else:
			u8 = 7/3
			p1 = 6-p1
			paths.append(2)
		if p1 < 3:
			p1 = p1-7
			paths.append(3)
		else:
			p1 = p1+p1
			x = x*8
			x = x*3
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))