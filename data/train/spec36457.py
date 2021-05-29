import numpy as np 

def function(x):

	m7 = 7
	t5 = x
	x = 2
	paths = []
	try:
		if m7 <= 3:
			t5 = x/t5
			m7 = m7+9
			paths.append(1)
		else:
			m7 = m7-6
			paths.append(2)
		if m7 <= 0:
			m7 = m7*x
			t5 = 5+t5
			paths.append(3)
		else:
			x = t5+1
			x = x*t5
			t5 = 7*t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))