import numpy as np 

def function(x):

	p7 = x
	t9 = x
	paths = []
	try:
		if p7 <= 7:
			t9 = t9+p7
			x = x*2
			p7 = p7+1
			paths.append(1)
		else:
			x = p7+6
			t9 = 1-7
			paths.append(2)
		if x <= 4:
			p7 = p7*6
			paths.append(3)
		else:
			t9 = 5/x
			p7 = 9/4
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		p7 = t9**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))