require('./env.js')
require('./source.js')


let c = '/api/sns/web/v1/homefeed'
let i = {
    'cursor_score': '',
    'num': 31,
    'refresh_type': 1,
    'note_index': 35,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed_recommend',
    'search_key': '',
    'need_num': 6,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': false,
}

//接口测试
function get_x_s(c,i) {
    return window._webmsxyw(c, i)
}
//
console.log(get_x_s(c,i))