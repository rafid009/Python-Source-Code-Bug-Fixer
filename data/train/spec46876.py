import numpy as np 

def function(x):

	b8 = 8
	t9 = 5
	paths = []
	try:
		if x > 4:
			t9 = t9/3
			b8 = 8/3
			paths.append(1)
		else:
			x = x/9
			x = x*t9
			t9 = 3+t9
			paths.append(2)
		if b8 <= 0:
			b8 = t9/8
			x = 6-x
			t9 = 2+2
			paths.append(3)
		else:
			t9 = t9+0
			t9 = t9+x
			t9 = b8*t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		b8 = t9**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))