from fastapi import APIRouter, status, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['hat', 'trousers', 'shirt', 'boots']


@router.post('/new')
def create_product(product_title: str = Form(...)):
    products.append(product_title)
    return {'message': product_title}


@router.get('/all')
def get_all_products():
    data = f'All you need to go outside is ' + ', '.join(products)
    response = Response(status_code=status.HTTP_404_NOT_FOUND,
                        content=data, media_type='text/plain')
    response.set_cookie(key='api_cookies', value=data, max_age=1000)
    return response


@router.get('/withheader')
def get_product_with_header(
    response: Response,
    custom_header: list[str] = Header([]),
    api_cookies: Optional[str] = Cookie(None)
):
    if custom_header:
        response.headers['custom-response-header'] = ', '.join(
            custom_header) + ', Another header'
    return {
        'data': products,
        'custom_header': custom_header,
        'api_cookies': api_cookies
    }


@router.get('/{id}', responses={
    status.HTTP_200_OK: {
        'content': {
            'text/html': {
                'example': '<div>Product</div>'
            }
        },
        'description': 'Returns the HTML for a product'
    },
    status.HTTP_404_NOT_FOUND: {
        'content': {
            'text/plain': {
                'example': 'Product not available'
            }
        },
        'description': 'A cleartext error message'
    },
})
def get_product(id: int):
    if id < 0 or id > len(products):
        output = 'Product not available'
        return PlainTextResponse(status_code=status.HTTP_404_NOT_FOUND, content=output, media_type='text/plain')

    product = products[id]
    output = f'''
            <head>
                <style>
                    .product {{
                        width: 100px;
                        height: 50px;
                        border: 2px solid black;
                        background-color: lightblue;
                        text-align: center;
                    }}
                </style>
            </head>
            <div class='product'>
                {product}
            </div>
        '''
    return HTMLResponse(status_code=status.HTTP_200_OK, content=output, media_type='text/html')
