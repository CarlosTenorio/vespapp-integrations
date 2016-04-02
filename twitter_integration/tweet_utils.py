class TweetUtils:

    @classmethod
    def is_valid(cls, tweet):
        is_valid = False
        if not tweet['in_reply_to_status_id'] and not "retweeted_status" in tweet:  # If tweet is not a reply
            if "extended_entities" in tweet and "media" in tweet['extended_entities']:
                is_valid = True
                for media_object in tweet['extended_entities']['media']:
                    if media_object['type'] != 'photo':
                        is_valid = False
                        break
        return is_valid

