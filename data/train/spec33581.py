import numpy as np 

def function(x):

	p7 = x
	t2 = x
	paths = []
	try:
		if p7 <= 2:
			t2 = x/t2
			p7 = x+2
			paths.append(1)
		else:
			t2 = t2+t2
			x = 9+x
			t2 = 3+4
			paths.append(2)
		if t2 <= 7:
			t2 = t2-5
			p7 = p7+9
			paths.append(3)
		else:
			t2 = x/2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		p7 = t2**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))